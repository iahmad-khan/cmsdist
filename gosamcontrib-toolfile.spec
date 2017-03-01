### RPM external gosamcontrib-toolfile 1.0
Requires: gosamcontrib
%prep

%build

%install

mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/form.xml
<tool name="gosamcontrib" version="@TOOL_VERSION@">
  <client>
    <environment name="GOSAMCONTRIB_BASE" default="@TOOL_ROOT@"/>
    <environment name="LIBDIR" default="$GOSAMCONTRIB_BASE/lib"/>
    <environment name="INCLUDE" default="$GOSAMCONTRIB_BASE/include"/>
    <environment name="BINDIR" default="$GOSAMCONTRIB_BASE/bin"/>
  </client>
  <runtime name="PATH" default="$BINDIR" type="path"/>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post

