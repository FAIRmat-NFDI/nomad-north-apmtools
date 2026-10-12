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
    # && mkdir -p "/tmp/aptyzer" \
    # && cd "/tmp/aptyzer" \
    # && git clone https://github.com/areichm/APTyzer.git \
    # && cd "APTyzer" \
    # && git checkout 39ab5e44c60f6f9e1c517f76b04914ac59e98bef \
    # && mkdir -p "${HOME}/aptyzer" \
    # && mv "/tmp/aptyzer/APTyzer/APTyzer_V_1_2o.ipynb" "${HOME}/aptyzer/aptyzer.ipynb" \
    # && chown ${NB_UID}:${NB_GID} "${HOME}/aptyzer/aptyzer.ipynb" \
    # && rm -rf "/tmp/aptyzer"

ENV PATH=${CONDA_PREFIX}/bin:${PATH}

RUN echo "conda activate apmtools" >> "${HOME}/.bashrc" \
    && chown ${NB_UID}:${NB_GID} "${HOME}/.bashrc"

RUN cd "${HOME}" \
    && git clone --recurse-submodules https://gitlab.com/paraprobe/paraprobe-toolbox.git \
    && cd "${HOME}/paraprobe-toolbox" \
    && git checkout v0.6.0 \
    && git submodule sync --recursive \
    && git submodule update --init --recursive \
    && pip install -e "./code/thirdparty/mandatory/pynxtools-apm[ipynb,batch]" \
    && pip install -e "."

RUN cd "${HOME}/paraprobe-toolbox" \
    && chmod +x ".scripts/linux/*" \
    && .scripts/linux/build.sh \
    && .scripts/linux/install.sh \
    && chmod +x ".code/paraprobe_*"

RUN fix-permissions "${HOME}/paraprobe-toolbox" \
    && chown -R ${NB_UID}:${NB_GID} "${HOME}/paraprobe-toolbox"

USER ${NB_UID}
WORKDIR "${HOME}"
