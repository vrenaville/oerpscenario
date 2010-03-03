###############################################################################
#
#    OERPScenario, OpenERP Functional Tests
#    Copyright 2009 Camptocamp SA
#
##############################################################################

@sale @addons @init
Feature Initialize the settings
  In order ensure the right state for the tests suite
  I want to set some parameters and settings
  
  Scenario: init_account_parameters
      Given I am loged as admin user with password admin used
      And the company currency is set to EUR 
      And the following currency rate settings are:
      |code|rate|name|
      |EUR|1.000|01-01-2009|
      |CHF|1.644|01-01-2009|
      |CHF|1.500|09-09-2009|
      |CHF|0.6547|10-10-2009|
      |USD|1.3785|01-01-2009|
      And a cash journal in USD exists
      And a cash journal in CHF exists
      And a cash journal in EUR exists
      And the demo data are loaded