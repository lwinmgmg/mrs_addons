# pylint: disable=pointless-statement,missing-module-docstring
{
    "name": "Medical Record System",
    "version": "1.0.0",
    "category": "medical",
    "summary": "Medical Record System",
    "description": "Medical Record System",
    "sequence": "1",
    "website": "https://www.cosmosmm.com",
    "author": "Lwin Maung Maung",
    "maintainer": "lwinmaungmaung@cosmosmm.com",
    "license": "LGPL-3",
    "support": "lwinmaungmaung@cosmosmm.com",
    "depends": ["base", "product", "mrs_patient"],
    "demo": [],
    "data": [
        "security/security_groups.xml",
        "security/ir.model.access.csv",
        "views/mrs_location_view.xml",
        "views/visit_view.xml",
        "views/menus.xml",
    ],
    "application": True,
    "installable": True,
}
