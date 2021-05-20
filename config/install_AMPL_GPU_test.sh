mkdir github
cd github
git clone https://github.com/stewarthe6/AMPL-1.git


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

patch -N /content/github/AMPL-1/atomsci/ddm/pipeline/transformations.py transformations_py.patch

cat << "EOF" > __init___py.patch
--- /content/AMPL-1/atomsci/ddm/__init__.py.backup    2020-09-19 18:10:05.264013977 +0000
+++ /content/AMPL-1/atomsci/ddm/__init__.py   2020-09-19 18:15:37.338771924 +0000
@@ -1,6 +1,6 @@
 import pkg_resources
 try:
     __version__ = pkg_resources.require("atomsci-ampl")[0].version
-except TypeError:
+except:
     pass
EOF

patch -N /content/github/AMPL-1/atomsci/ddm/__init__.py __init___py.patch

cat << "EOF" > featurization_py.patch
--- a/atomsci/ddm/pipeline/featurization.py
+++ b/atomsci/ddm/pipeline/featurization.py
@@ -732,7 +732,7 @@ class DynamicFeaturization(Featurization):
             ##JEA: will set weights to 0 for missing values
             ##JEA: Featurize task results iff they exist.
             dset_df=dset_df.replace(np.nan, "", regex=True)
-            vals, w = dl.convert_df_to_numpy(dset_df, params.response_cols) #, self.id_field)
+            vals, w = dl._convert_df_to_numpy(dset_df, params.response_cols) #, self.id_field)
             # Filter out examples where featurization failed.
             vals, w = (vals[is_valid], w[is_valid])
         else:
EOF

patch -N /content/github/AMPL-1/atomsci/ddm/pipeline/featurization.py featurization_py.patch


PATH=/content/AMPL-1/bin:$PATH
PYTHONPATH=

cd /content/github/AMPL-1
git checkout version_colab_bug
./build.sh
./install.sh system
