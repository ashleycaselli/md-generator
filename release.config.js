let publishCmd = `
IMAGE_NAME_LOWER=$(echo "$IMAGE_NAME" | tr '[:upper:]' '[:lower:]')
docker build --build-arg poetry_version=$POETRY_VERSION -t "$REGISTRY/$IMAGE_NAME_LOWER:\${nextRelease.version}" -t "$REGISTRY/$IMAGE_NAME_LOWER:latest" .
docker push --all-tags "$REGISTRY/$IMAGE_NAME_LOWER"
`
let config = require('semantic-release-preconfigured-conventional-commits');
config.plugins.push(
    [
        "@semantic-release/exec",
        {
            "publishCmd": publishCmd
        }
    ],
    "@semantic-release/github",
    "@semantic-release/git"
)
module.exports = config