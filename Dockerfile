# INTENTIONALLY VULNERABLE DOCKERFILE - FOR SECURITY SCANNER TESTING ONLY
# Uses old base image with known CVEs to trigger Trivy container scanning.

FROM node:14-alpine

# C2C Mapping Labels (Method 2) - MDC reads these from image manifest
# See: Labels Used Today for C2C Mapping (Inbal's C2C Tech Prereq doc)
# Dynamic values are overridden at build time by docker/metadata-action

# 1. OCI standard label - primary label MDC uses for GitHub repos
LABEL org.opencontainers.image.source="https://github.com/zava-corporation/zava-shift-left-demo"

# 2. Legacy label-schema equivalent - MDC also checks this
LABEL org.label-schema.vcs-url="https://github.com/zava-corporation/zava-shift-left-demo"

# 3. Azure DevOps labels - MDC uses these for ADO-built images
LABEL com.azure.dev.image.build.repository.uri="https://github.com/zava-corporation/zava-shift-left-demo"
LABEL com.visualstudio.msazure.image.build.repository.uri="https://github.com/zava-corporation/zava-shift-left-demo"

# Additional metadata
LABEL org.opencontainers.image.description="Shift-left security demo - intentionally vulnerable"
LABEL org.opencontainers.image.vendor="Zava Corporation"
LABEL org.opencontainers.image.licenses="MIT"

# Run as root (security issue)
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

ENV NODE_ENV=development
ENV PORT=3000

CMD ["node", "src/app.js"]
