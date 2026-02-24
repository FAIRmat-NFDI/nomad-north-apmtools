ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
ARG PLUGIN_NAME=nomad-north-apmtools

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN apt update \
 && apt-get install --no-install-recommends -y \
        m4 \
        file \
        build-essential \
        mpich \
        libgmp-dev \
        libmpfr-dev \
        libssl-dev \
        hwloc \
        git \
        wget \
        libgl1 \
        libglu1-mesa \
        libglu1-mesa-dev \
 && rm -rf /var/lib/apt/lists/*

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}

COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_apmtools/north_tools/apmtools/environment.yml" "/tmp/environment.yml"
COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_apmtools/north_tools/apmtools/example" "example"

# see nomad-north-nionswift plugins Dockerfile on how to possibly make that copy layering slimmer

# RUN mamba install --yes \
#       'nomkl' \
#       'paraprobe' \
#       'apav' \
#  && mamba clean --all -f -y \
#  && fix-permissions "${CONDA_DIR}" \
#  && fix-permissions "/home/${NB_USER}"

# Create the named environment with packages as mentioned in the environment.yml file, clear mamba cache
ARG env_name=apmtools
RUN mamba env create -f "/tmp/environment.yml" \
    && mamba clean --all -f -y \
    && rm -rf "/tmp/environment.yml"

# Register environment as Jupyter kernel
RUN conda run -n ${env_name} python -m ipykernel install --user --name="${env_name}" \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"

RUN echo "\n# Automatically activate nionswift environment" >> "/home/${NB_USER}/.bashrc" \
    && echo "conda activate nionswift" >>/home/${NB_USER}/.bashrc"

# Optional: make env default for subsequent RUN commands
# SHELL ["conda", "run", "-n", "apmtools", "/bin/bash", "-c"]

WORKDIR "${HOME}"

# Get rid of the following message when you open a terminal in jupyterlab:
# groups: cannot find name for group ID 11320
RUN touch ${HOME}/.hushlogin
