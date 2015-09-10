from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.cram')

name = "snakepit"
default_task = "publish"
version = '0.0.2.dev0'


@init
def set_properties(project):
    project.set_property('install_dependencies_upgrade', True)
    project.build_depends_on("mock")
    project.depends_on("jinja2")
    project.depends_on("pyyaml")
    project.depends_on("docopt")
