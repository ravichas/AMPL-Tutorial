mkdir github
cd github
git clone https://github.com/ATOMconsortium/AMPL.git

cat << "EOF" > transformations_py.patch
--- transformations.py  2020-09-14 17:08:22.225747322 -0700
+++ transformations_patched.py  2020-09-14 17:08:07.869651225 -0700
@@ -9,7 +9,7 @@

 import numpy as np
 import pandas as pd
-import umap
+# import umap

 import deepchem as dc
 from deepchem.trans.transformers import Transformer, NormalizationTransformer
EOF

patch -N /content/github/AMPL/atomsci/ddm/pipeline/transformations.py transformations_py.patch

PATH=/content/AMPL/bin:$PATH
PYTHONPATH=

cd /content/github/AMPL
./build.sh
./install.sh system
