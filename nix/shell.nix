let
  pkgs = import (fetchTarball
    "https://github.com/NixOS/nixpkgs/archive/970e93b9f82e2a0f3675757eb0bfc73297cc6370.tar.gz")
    { };
  myPython = pkgs.python312;
  pythonPackages = pkgs.python312Packages;

  pythonWithPkgs = myPython.withPackages (pythonPkgs:
    with pythonPkgs; [
      ipython
      pip
      debugpy
      setuptools
      virtualenvwrapper
      wheel
      grpcio
    ]);

  extraBuildInputs = with pythonPackages; [ ] ++ (with pkgs; [ ]);
in import ./python-shell.nix {
  extraBuildInputs = extraBuildInputs;
  # extraLibPackages = extraLibPackages;
  myPython = myPython;
  pythonWithPkgs = pythonWithPkgs;
  pkgs = pkgs;
}
