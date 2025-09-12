# -*- coding: utf-8 -*-
{
    "name": "Marshmallow Website",
    "summary": """
    """,
    "description": """
    """,
    "category": "Website/Website",
    "version": "18.0.1.0",
    "installable": True,
    "application": False,
    "auto_install": True,
    "depends": ["website"],
    "data": ["views/webclient_templates.xml", "data/pages.xml"],
    "assets": {
        "web.assets_frontend": [
            "marshmallow/static/src/css/global.css",
            "marshmallow/static/src/css/style.css",
        ],
    },
    "license": "LGPL-3",
}
