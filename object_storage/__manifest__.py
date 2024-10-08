# pylint: disable=pointless-statement,missing-module-docstring,duplicate-code
{
    "name": "Object Storage Connector",
    "version": "1.0.0",
    "category": "tools",
    "summary": "Object Storage Connector",
    "description": "Object Storage Connector",
    "sequence": "1",
    "website": "https://www.cosmosmm.com",
    "author": "Lwin Maung Maung",
    "maintainer": "lwinmaungmaung@cosmosmm.com",
    "license": "LGPL-3",
    "support": "lwinmaungmaung@cosmosmm.com",
    "depends": ["base"],
    "demo": [],
    "data": [
        "security/ir.model.access.csv",
        "data/os_attachment_gc_cron.xml",
        "data/os_attachment_type_data.xml",
        "views/os_attachment_view.xml",
    ],
    "external_dependencies": {"boto3": "1.*"},
    "application": True,
    "installable": True,
}
