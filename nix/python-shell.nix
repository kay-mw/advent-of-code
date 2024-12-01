{ pkgs ? import (fetchTarball
  "https://github.com/NixOS/nixpkgs/archive/4284c2b73c8bce4b46a6adf23e16d9e2ec8da4bb.tar.gz")
  { }, extraBuildInputs ? [ ], myPython ? pkgs.python3, extraLibPackages ? [ ]
, pythonWithPkgs ? myPython }:

let
  buildInputs = with pkgs;
    [ clang llvmPackages_16.bintools rustup ] ++ extraBuildInputs;

  lib-path = with pkgs; lib.makeLibraryPath buildInputs;

  shell = pkgs.mkShell {
    buildInputs = [
      pythonWithPkgs

      pkgs.readline
      pkgs.libffi
      pkgs.openssl

      pkgs.git
      pkgs.openssh
      pkgs.rsync
    ] ++ extraBuildInputs;
    shellHook = ''
      SOURCE_DATE_EPOCH=$(date +%s)

      export "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${lib-path}:${pkgs.stdenv.cc.cc.lib}/lib"

      export PYTHONPATH=$PYTHONPATH:`pwd`/$VENV/${myPython.sitePackages}/

      zsh
    '';
  };

in shell
