# INTENTIONALLY VULNERABLE DOCKERFILE - FOR SECURITY SCANNER TESTING ONLY
# Uses old base image with known CVEs to trigger Trivy container scanning.

FROM node:14-alpine

# Run as root (security issue)
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

ENV NODE_ENV=development
ENV PORT=3000

CMD ["node", "src/app.js"]
