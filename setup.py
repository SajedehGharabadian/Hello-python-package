from setuptools import setup

def preinstall():
    f = open("readme.md","r")
    text = f.read()
    return text


setup(name="Hello_python_package",version="1.0.0",
      author="Sajedeh Gharabadiyan",
      description="first package for test",
      requires=[],
      author_email="gharabadiyansajedeh@gmail.com",
      packages=["Hello_python_package"],
      long_description=open("readme.md", 'r').read(),
      long_description_content_type='text/markdown'
    )