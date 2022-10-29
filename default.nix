{ pgs ? import <nixpkgs> {} }:
	let
	my-python = pgs.python310Packages;
	in
	my-python.buildPythonPackage rec {
		name = "dbquaest";
		src = ./src;
		propagatedBuildInputs = with my-python; [
			numpy
			jupyterlab
			scipy
			];
	}
