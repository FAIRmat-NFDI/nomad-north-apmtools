ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
ARG PLUGIN_NAME=nomad-north-apmtools

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# with pre-existing NB_USER="jovyan" and NB_UID=100, NB_GID=1000
ENV HOME=/home/${NB_USER}

# low-level numerics and parallelization dependencies mainly for CGAL part of paraprobe-toolbox
# and for apps with QT GUI needs apav, apyt, pyccapt, aptyzer
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

COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_apmtools/north_tools/apmtools/environment.yml" "/tmp/environment.yml"
COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_apmtools/north_tools/apmtools/example" "${HOME}/example"
# see nomad-north-nionswift plugins Dockerfile on how to possibly make that copy layering slimmer

# Create the named environment with packages as mentioned in the environment.yml file, clear mamba cache
# ARG env_name=apmtools
RUN mamba env create -f "/tmp/environment.yml" \
    && mamba clean --all -f -y \
    && rm -rf "/tmp/environment.yml" \
    && mkdir -p "/tmp/aptyzer" \
    && cd "/tmp/aptyzer" \
    && git checkout 39ab5e44c60f6f9e1c517f76b04914ac59e98bef \
    && cp "/tmp/aptyzer/APTyzer/APTyzer_V_1_2o.ipynb" "${HOME}/aptyzer/aptyzer.ipynb" \
    && rm -rf "/tmp/aptyzer"

# Register environment as Jupyter kernel
RUN conda run -n ${env_name} python -m ipykernel install --user --name=apmtools \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "${HOME}"

RUN echo "\n# Automatically activate apmtools environment" >> "${HOME}/.bashrc" \
    && echo "conda activate apmtools" >>"${HOME}/.bashrc" \
    && chown ${NB_UID}:${NB_GID} "${HOME}/.bashrc"

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}

# Optional: make env default for subsequent RUN commands
SHELL ["conda", "run", "-n", "apmtools", "/bin/bash", "-c"]

WORKDIR "${HOME}"

