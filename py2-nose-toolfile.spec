### RPM external py2-nose-toolfile 1.0
Requires: py2-nose
%prep

%build

%install

mkdir -p %{i}/etc/scram.d
cat << \EOF_TOOLFILE >%{i}/etc/scram.d/py2-nose.xml
<tool name="py2-nose" version="@TOOL_VERSION@">
  <info url="https://pypi.python.org/pypi/nose"/>
  <client>
    <environment name="PY2_NOSE" default="@TOOL_ROOT@"/>
    <environment name="LIBDIR" default="$PY2_NOSE/lib"/>
    <runtime name="PYTHONPATH" value="$PY2_NOSE/lib/python@PYTHONV@/site-packages" type="path"/>
  </client>
</tool>
EOF_TOOLFILE

export PYTHONV=$(echo $PYTHON_VERSION | cut -f1,2 -d.)

## IMPORT scram-tools-post

