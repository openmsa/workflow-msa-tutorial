#!/bin/bash
. /usr/share/install-libraries/il-lib.sh

pushd /opt/fmc_repository/Process || exit;
emit_step "Linking Workflow Tutorial."
mk_meta_link "OpenMSA_Workflow_Tutorials" "Tutorials"
popd || exit

pushd /opt/fmc_repository/CommandDefinition || exit;
emit_step "Linking Microservice Tutorial."
mk_meta_link "OpenMSA_Workflow_Tutorials" "Tutorials"
popd || exit
