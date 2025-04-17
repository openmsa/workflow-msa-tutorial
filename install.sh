#!/bin/bash
. /usr/share/install-libraries/il-lib.sh

pushd /opt/fmc_repository/Process || exit;
emit_step "Linking Tutorial."
mk_meta_link "OpenMSA_Workflow_Tutorials" "Tutorials"
popd || exit

pushd /opt/fmc_repository/CommandDefinition || exit;
emit_step "Linking Microservice Tutorial."
ln -fs ../OpenMSA_Workflow_Tutorials/Microservices/.meta_LINUX_Tutorials .meta_LINUX_Tutorials
ln -fs ../OpenMSA_Workflow_Tutorials/Microservices/LINUX_Tutorials LINUX_Tutorials
popd || exit

chown -R ncuser:ncuser /opt/fmc_repository/



