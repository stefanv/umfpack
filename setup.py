import setuptools

subpackage = 'umfpack'
version = '5.1.0'

def configuration(parent_package = '', top_path = None):
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info, dict_append

    config = Configuration( None, parent_package, top_path,
                            namespace_packages = ['scikits'] )
    config.set_options(
        ignore_setup_xxx_py = True,
        assume_default_configuration = True,
        delegate_options_to_subpackages = True,
        quiet = True,
    )

    config.add_subpackage('scikits.umfpack')
    config.add_data_files('scikits/__init__.py')

    return config

def setup_package():

    from numpy.distutils.core import setup

    setup(
        name = 'scikits.' + subpackage,
        version = version,
        maintainer = "Robert Cimrman",
        maintainer_email = "robert.cimrman@gmail.com",
        description = "Python interface to the UMFPACK sparse linear solver.",
        url = "http://www.scipy.org",
        license = 'BSD',
        configuration = configuration,
        install_requires = [
            'numpy',
            'scipy',
        ],
    )
    return

if __name__ == '__main__':
    setup_package()
