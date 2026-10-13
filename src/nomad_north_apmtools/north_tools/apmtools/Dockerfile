ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
ARG PLUGIN_NAME=nomad-north-apmtools

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# with pre-existing NB_USER="jovyan" and NB_UID=100, NB_GID=1000
ENV HOME=/home/${NB_USER}
ENV CONDA_DIR=/opt/conda
ENV CONDA_PREFIX=/opt/conda/envs/apmtools

RUN apt-get update \
   && apt-get install --no-install-recommends -y \
        m4 \
        file \
        wget \
        libgl1 \
        libglu1-mesa \
        libglu1-mesa-dev \
   && rm -rf /var/lib/apt/lists/*

COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_apmtools/north_tools/apmtools/environment.yml" "/tmp/environment.yml"
COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_apmtools/north_tools/apmtools/example" "${HOME}/example"

RUN mamba env create -f "/tmp/environment.yml" \
    && mamba clean --all -f -y \
    && conda run -n apmtools python -m ipykernel install --user --name=apmtools \
    && mkdir -p "${CONDA_PREFIX}/lib/hdf5/plugin" \
    && cp ${CONDA_PREFIX}/lib/python3.12/site-packages/hdf5plugin/plugins/*.so "${CONDA_PREFIX}/lib/hdf5/plugin/" \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "${CONDA_PREFIX}" \
    && rm -rf "/tmp/environment.yml"

# see v0.1.4 on how to add A. Reichmann's aptyzer but dropped it because is no longer maintained

ENV PATH=${CONDA_PREFIX}/bin:${PATH}

RUN echo "conda activate apmtools" >> "${HOME}/.bashrc" \
    && chown ${NB_UID}:${NB_GID} "${HOME}/.bashrc"

RUN cd "${HOME}" \
    && git clone --recurse-submodules https://gitlab.com/paraprobe/paraprobe-toolbox.git \
    && cd "${HOME}/paraprobe-toolbox" \
    && git checkout "main" \
    && git submodule sync --recursive \
    && git submodule update --init --recursive \
    && pip install -e "./code/thirdparty/mandatory/pynxtools-apm[ipynb,batch]" \
    && pip install -e "."

RUN cd "${HOME}/paraprobe-toolbox" \
    && chmod +x "scripts/linux/build.sh" \
    && chmod +x "scripts/linux/install.sh" \
    && ./scripts/linux/build.sh "${CONDA_PREFIX}" \
    && ./scripts/linux/install.sh \
    && chmod +x "code/paraprobe_ranger" \
               "code/paraprobe_selector" \
               "code/paraprobe_surfacer" \
               "code/paraprobe_distancer" \
               "code/paraprobe_tessellator" \
               "code/paraprobe_spatstat" \
               "code/paraprobe_nanochem" \
               "code/paraprobe_intersector" \
    && fix-permissions "${HOME}/paraprobe-toolbox" \
    && chown -R ${NB_UID}:${NB_GID} "${HOME}/paraprobe-toolbox"

# && rm -rf "code/utils/build" \

USER ${NB_UID}
WORKDIR "${HOME}"
