from setuptools import setup


setup(
    zip_safe=True,
    name='jeeves-minion',
    version='0.1',
    author='adaml',
    author_email='adam.lavie@gmail.com',
    packages=[
        'jeeves_minion',
        'jeeves_minion.stream',
        'jeeves_minion.stream.resources'
    ],
    license='LICENSE',
    description='Jeeves-CI is a distributed task engine for dispatching jobs '
                'on clean docker/vms environments across workers.',
    install_requires=[
        'celery==4.2.1',
        'docker==2.1',
        'tornado==4.2',
        'pyyaml==3.13',
        'psycopg2==2.7.1',
    ],
    package_data={
        'jeeves_minion': ['stream/resources/*.html'],
        'jeeves_minion.stream': ['resources/static/*.js'],
        'web_ui.resources': ['static/*.js'],
    },
    include_package_data=True,
)
