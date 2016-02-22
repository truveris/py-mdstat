How to release py-mdstat
========================
Follow these steps:
- Change the version in ``setup.py`` and ``mdstat/__init__.py``
- Update the release date and version in ``CHANGES.txt``
- Commit, push
- Create and push a new tag::
    git tag -a X.Y.Z -m 'Releasing vX.Y.Z'
    git push --tags
- Download the release tarball from github (release section),
- Sign it::
    gpg --armor --detach-sig py-mdstat-X.Y.Z.tar.gz
- Distribute on Pypi::
    python setup.py sdist upload
