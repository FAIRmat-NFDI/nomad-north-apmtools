# apmtools - NORTH tool

This directory contains the configuration for the apmtools NORTH (NOMAD Remote Tools Hub) tool and NOMAD plugin.

## Quick start

The apmtools NORTH tool provides a containerized environment defined in a `NORTHTool` definition, a `NorthToolEntryPoint`, and a Dockerfile.

## Building and testing

Build the Docker image locally:

```bash
docker build -f src/nomad_north_apmtools/north_tools/apmtools/Dockerfile \
    -t ghcr.io/fairmat-nfdi/nomad-north-apmtools:latest .
```

Test the image (for jupyter notebook image):

```bash
docker run -p 8888:8888 ghcr.io/fairmat-nfdi/nomad-north-apmtools:latest
```

Access JupyterLab at `http://localhost:8888`.

## Documentation

For comprehensive documentation on creating and managing NORTH tools, including e.g.,

- Entry point configuration and `NORTHTool` API
- Docker image structure and best practices
- Dependency management

See the [NOMAD NORTH Tools documentation](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html).
