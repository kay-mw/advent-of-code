{
  description = "advent-of-code";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/59b6c96beacc898566c9be1052ae806f3835f87d";
  };

  outputs =
    { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
    in
    {
      devShells."${system}".default =
        let
          pkgs = import nixpkgs { inherit system; };
        in
        pkgs.mkShell {
          packages = with pkgs; [
            python314
            (haskellPackages.ghcWithPackages (hpkgs: with hpkgs; [ cabal-install ]))
          ];
        };
    };
}
