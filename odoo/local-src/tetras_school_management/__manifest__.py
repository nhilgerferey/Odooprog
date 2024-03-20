{
    "name": "Tetras - School Management",
    "version": "17.0.1.0.0",
    "depends": ["base"],
    "author": "Kal-It",
    "website": "https://kal-it.fr",
    "license": "GPL-3 or any later version",
    "category": "Tools",
    "data": [
        "security/ir.model.access.csv",
        "views/grade_views.xml",
        "views/student_views.xml",
        "views/teacher_views.xml",
        "views/classroom_views.xml",
        "views/control_views.xml",
        "views/menu_views.xml",
        "views/tetras_assets_index.xml",
    ],
    "assets": {
        "tetras_school_management._assets_tetras": [

            # 'webclient' bootstrap customization layer
            ('include', 'web._assets_helpers'),
            ('include', 'web._assets_backend_helpers'),

            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',

            # Import Bootstrap
            ('include', 'web._assets_bootstrap_backend'),

            # Icons
            'web/static/src/libs/fontawesome/css/font-awesome.css',
            'web/static/lib/odoo_ui_icons/*',
            'web/static/src/webclient/icons.scss',

            # scss variables and utilities
            'web/static/src/scss/bootstrap_overridden.scss',
            'web/static/src/scss/fontawesome_overridden.scss',
            'web/static/fonts/fonts.scss',

            # JS boot
            'web/static/src/module_loader.js',

            # libs (should be loaded before framework)
            'web/static/lib/luxon/luxon.js',
            'web/static/lib/owl/owl.js',
            'web/static/lib/owl/odoo_module.js',

            # JS framework
            ('include', 'web._assets_core'),
            ('remove', 'web/static/src/core/errors/error_handlers.js'),

            "tetras_school_management/static/src/**/*",

            # main.js boots the pos app, it is only included in the prod bundle as tests mount the app themselves
            ('remove', 'tetras_school_management/static/src/app/main.js'),
        ],
        'tetras_school_management.assets_prod': [
            ('include', 'tetras_school_management._assets_tetras'),
            'tetras_school_management/static/src/app/main.js',
        ],
    }

}
