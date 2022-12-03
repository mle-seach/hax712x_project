from setuptools import setup
from Trackelec import __version__ as current_version

setup(
    name="trackelec",
    version=current_version,
    description="Visualization and prediction of the french electricity consumption",
    url="https://github.com/mle-seach/hax712x_project.git",
    author="Thibault FERRETTI, Sarah MATOUB, Pauline DUSFOUR-CASTAN, Mathieu LE-SEACH, Guillaume BERNARD-REYMOND",
    author_email="thibault.ferretti@etu.umontpellier.fr",
    license="MIT",
    packages=["trackelec", "trackelec.predic", "trackelec.visu"],
    zip_safe=False,
)
