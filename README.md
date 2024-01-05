[![CI](https://github.com/ashleycaselli/md-generator/actions/workflows/build-release.yml/badge.svg)](https://github.com/ashleycaselli/md-generator/actions/workflows/build-release.yml)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

# How to

The Markdown files can be generated with the following
command `docker run -v $(pwd):/app ghcr.io/ashleycaselli/md-generator`.

**NB:** the default configuration requires a `refs.bib` file in the current working directory (`$pwd`). The output files can
be found in the `pubs` folder that will be created in the current working directory.

In case you would like to change the input/output configuration, you can do it using environment variables.

`BIB_FILE`: name of the `.bib` file with the references
`OUT_PATH`: path of the output directory

### Example by passing the env vars inline
`docker run -v $(pwd)/tmp:/app/tmp --env BIB_FILE=tmp/refs.bib --env OUT_PATH=tmp/ ghcr.io/ashleycaselli/md-generator`

### Example by passing the env vars using a file
`docker run -v $(pwd)/tmp:/app/tmp --env-file .env ghcr.io/ashleycaselli/md-generator`

# Credits

This project was forked and originally based on the work of [Stuart Geiger](https://github.com/staeiou).
