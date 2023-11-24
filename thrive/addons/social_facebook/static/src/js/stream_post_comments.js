/** @thrive-module **/

import { StreamPostComments } from '@social/js/stream_post_comments';
import { StreamPostCommentListFacebook } from './stream_post_comment_list';
import { StreamPostCommentsReplyFacebook } from './stream_post_comments_reply';
import { onWillStart } from "@thrive/owl";

export class StreamPostCommentsFacebook extends StreamPostComments {

    setup() {
        super.setup();

        this.totalLoadedComments = this.props.comments.length;
        this.nextRecordsToken = this.props.nextRecordsToken;
        this.commentsCount = this.props.commentsCount;
        this.state.showLoadMoreComments = this.totalLoadedComments < this.props.summary.total_count;

        onWillStart(async () => {
            const facebookInfo = await this.orm.read(
                'social.account', [this.props.accountId], ['name', 'facebook_account_id']);

            this.mediaSpecificProps = Object.assign(this.mediaSpecificProps, {
                accountId: this.props.accountId,
                accountName: facebookInfo[0].name,
                pageFacebookId: facebookInfo[0].facebook_account_id,
            });
        });
    }

    async loadMoreComments() {
        const nextComments = await this.rpc('/social_facebook/get_comments', {
            stream_post_id: this.originalPost.id.raw_value,
            next_records_token: this.nextRecordsToken,
            comments_count: this.commentsCount
        });

        this.totalLoadedComments += nextComments.comments.length;
        if (this.totalLoadedComments >= this.props.summary.total_count) {
            this.state.showLoadMoreComments = false;
        }
        this.comments.push(...nextComments.comments);
        this.nextRecordsToken = nextComments.nextRecordsToken;
    }

    get commentListComponent() {
        return StreamPostCommentListFacebook;
    }

    get commentReplyComponent() {
        return StreamPostCommentsReplyFacebook;
    }

}
