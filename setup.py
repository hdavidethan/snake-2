import pip

# Get the list of packages to install
packages = ["torch", "torchvision", "matplotlib", "IPython"]

# Install the packages
for package in packages:
    pip.main(["install", package])