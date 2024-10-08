# pylint: disable=pointless-statement,missing-module-docstring,duplicate-code
{
    "name": "Medical Record System Diagnosis",
    "version": "1.0.0",
    "category": "medical",
    "summary": "Medical Record System Diagnosis",
    "description": "Medical Record System Diagnosis",
    "sequence": "1",
    "website": "https://www.cosmosmm.com",
    "author": "Lwin Maung Maung",
    "maintainer": "lwinmaungmaung@cosmosmm.com",
    "license": "LGPL-3",
    "support": "lwinmaungmaung@cosmosmm.com",
    "depends": ["mrs_mrs"],
    "demo": [],
    "data": [
        "security/ir.model.access.csv",
        "views/diagnosis_view.xml",
        "views/visit_diagnosis_view.xml",
        "views/diagnosis_condition_view.xml",
        "views/res_partner_view.xml",
        "views/menus.xml",
    ],
    "application": True,
    "installable": True,
}
