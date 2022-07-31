import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='Recommendation_Engine',
    version='0.0.1',
    author='Oricha Abdulrasheed',
    author_email='am4rash@gmail.com',
    description='Recommendation Engine',
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url='https://github.com/zkyte/Recommendation_Engine',
    project_urls={
        "Bug Tracker": "https://github.com/zkyte/Recommendation_Engine/issues"
    },
    license='MIT',
    packages=['Recommendation_Engine'],
    install_requires=['joblib==1.0.1', 'numpy==1.21.2', 'pandas==1.3.3', 'python-dateutil==2.8.2', 'pytz==2021.3',
                      'scikit-learn==1.0', 'scipy==1.7.1', 'six==1.16.0', 'sklearn==0.0', 'threadpoolctl==3.0.0'],
)
