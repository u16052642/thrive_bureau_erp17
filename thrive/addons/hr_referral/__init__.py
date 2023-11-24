# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

def _update_stage(env):
    for (stage_ref, points) in [
        ("hr_recruitment.stage_job1", 5),
        ("hr_recruitment.stage_job2", 10),
        ("hr_recruitment.stage_job3", 15),
        ("hr_recruitment.stage_job4", 20),
        ("hr_recruitment.stage_job5", 50),
    ]:
        stage = env.ref(stage_ref, raise_if_not_found=False)
        if stage:
            stage.points = points


from . import models
from . import report
from . import wizard


def _pre_init_referral(env):
    # When installing hr_referral, ref_user_id will always be equal to False.
    # We create this column now instead of ORM. If this column is already created, the ORM will not create it again and the compute function will not be called.
    # In case of huge database, the function _compute_ref_user_id can be time consumming and always return False.
    env.cr.execute("ALTER TABLE hr_applicant ADD COLUMN ref_user_id int4 REFERENCES res_users(id)")
