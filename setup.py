from setuptools import setup

if __name__ == "__main__":
    setup(
        name="lbo",
        version="0.0.1",
        install_requires=[
            "ipykernel",
            "matplotlib",
            "numpy",
            "omegaconf",
            "scikit-optimize",
            "tqdm",
        ],
        author="Mavi, Derek, Shay",
        author_email="ssnyde9@gmu.edu",
        description = "Bayesian Optimization in Lava",
        maintainer="Mavi, Derek, Shay",
        maintainer_email="ssnyde9@gmu.edu",
        packages=["lbo"]
    )