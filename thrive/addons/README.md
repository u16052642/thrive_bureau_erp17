[![Build Status](http://runbot.thrivebureau.com/runbot/badge/flat/7/master.svg)](http://runbot.thrivebureau.com/runbot/repo/git-github-com-thrive-enterprise-7)
[![Tech Doc](http://img.shields.io/badge/14.0-docs-875A7B.svg?style=flat)](http://www.thrivebureau.com/documentation/master)
[![Help](http://img.shields.io/badge/master-help-875A7B.svg?style=flat)](https://www.thrivebureau.com/forum/help-1)
[![Nightly Builds](http://img.shields.io/badge/master-nightly-875A7B.svg?style=flat)](http://nightly.thrivebureau.com/)

Thrive
----

Thrive is a suite of web based open source business apps.

The main Thrive Apps include an <a href="https://www.thrivebureau.com/app/crm">Open Source CRM</a>,
<a href="https://www.thrivebureau.com/app/website">Website Builder</a>,
<a href="https://www.thrivebureau.com/app/ecommerce">eCommerce</a>,
<a href="https://www.thrivebureau.com/app/inventory">Warehouse Management</a>,
<a href="https://www.thrivebureau.com/app/project">Project Management</a>,
<a href="https://www.thrivebureau.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.thrivebureau.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.thrivebureau.com/app/employees">Human Resources</a>,
<a href="https://www.thrivebureau.com/app/lead-automation">Marketing</a>,
<a href="https://www.thrivebureau.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.thrivebureau.com/app/purchase">Purchase Management</a>,
<a href="https://www.thrivebureau.com/">...</a>

Thrive Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.thrivebureau.com">Open Source ERP</a> when you install several Apps.

Getting started with Thrive
-------------------------

For a standard installation please follow the <a href="https://www.thrivebureau.com/documentation/17.0/administration/install/install.html">Setup instructions</a>
from the documentation.

If you are a developer you may type the following command at your terminal:

    wget -O- https://raw.githubusercontent.com/thrive/thrive/master/setup/setup_dev.py | python

Then follow <a href="https://www.thrivebureau.com/documentation/17.0/developer/howtos.html">the developer tutorials</a>

For Thrive employees
------------------

To add the thrive-dev remote use this command:

    $ ./setup/setup_dev.py setup_git_dev

To fetch thrive merge pull requests refs use this command:

    $ ./setup/setup_dev.py setup_git_review
