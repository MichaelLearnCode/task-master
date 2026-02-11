# --- STAGE 1: Install dependencies ---
FROM node:20-alpine AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# --- STAGE 2: Build the application ---
FROM node:18-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
# Biến môi trường lúc build (nếu cần)
ENV NEXT_TELEMETRY_DISABLED 1
RUN npm run build

# --- STAGE 3: Production runner ---
FROM node:18-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

# Tạo user để không chạy bằng quyền root (bảo mật)
RUN addgroup --system --gid 1001 taskmaster
RUN adduser --system --uid 1001 michael

# Copy các file cần thiết từ stage builder
COPY --from=builder --chown=michael:taskmaster /app/public ./public
COPY --from=builder --chown=michael:taskmaster /app/.next/standalone ./
COPY --from=builder --chown=michael:taskmaster /app/.next/static ./.next/static

USER michael

EXPOSE 3003
ENV PORT=3003

# Chạy server bằng file server.js do Next.js standalone sinh ra
CMD ["node", "server.js"]