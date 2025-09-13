# -*- coding: utf-8 -*-
{
    "name": "VIVA - Professional Website Theme",
    "summary": "Modern, responsive website theme with streaming services focus",
    "description": """
        A comprehensive website theme designed for streaming and telecommunications services.
        Features include:
        - Modern, accessible header with navigation for Residential, Commercial, and Support services
        - Professional footer with call-to-action sections and service links
        - Responsive design optimized for all devices
        - Clean, modern styling with custom CSS framework
        - SEO-friendly structure with proper semantic HTML
        - Integration-ready for Odoo 18 website module
        - Customizable color scheme and branding elements
        - Mobile-first responsive design approach
    """,
    "category": "Website/Theme",
    "version": "18.0.1.0.0",
    "installable": True,
    "application": False,
    "auto_install": False,
    "depends": ["base", "website"],
    "data": [
        "views/webclient_templates.xml",
        "data/pages.xml",
    ],
    "assets": {
        'web.assets_frontend': [
            'viva_theme_website/static/src/**/*',
            # 'viva_theme_website/static/src/img/**/*',
        ],
    },
    "license": "LGPL-3",
    "author": "Andrew",
    "website": "",
}