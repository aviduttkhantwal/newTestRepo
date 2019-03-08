def cmd_wui(argv, path_to_tx):
    """Run a web UI."""
    from flask import Flask, flash, jsonify, render_template, request
    import webbrowser
    app = Flask(__name__)


    @app.route('/tx/index/')
    def index():
        """Load start page where you select your project folder
        or load history projects from local DB."""
        from txclib import get_version
        txc_version = get_version()
        prj = project.Project(path_to_tx)

        # Let's create a resource list from our config file
        res_list = []
        prev_proj = ''
        for idx, res in enumerate(prj.get_resource_list()):
                hostname = prj.get_resource_host(res)
        username, password = prj.getset_host_credentials(hostname)
        return render_template('init.html', txc_version=txc_version, username=username)
