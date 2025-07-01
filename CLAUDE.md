# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Tennis Court Booking Bot - A minimal React + FastAPI application for people to easily set up bots to book tennis courts.

# Development Instructions

implment minimal changes, don't over engineering

## Development Commands

### Frontend
```bash
pnpm install
pnpm run dev  # Port 8080
```

### Backend
```bash
cd backend
pip install -r requirements.txt
python run.py  # Port 8000
```

## Architecture

### Simple Structure
- Frontend: Single React component (`src/App.tsx`)
- Backend: Single FastAPI file (`backend/app/main.py`)
- Minimal dependencies, no over-engineering

### Key Files
- `src/App.tsx` - Main React component with 3 features
- `backend/app/main.py` - FastAPI with 5 endpoints
- `backend/run.py` - Simple run script

## Features

1. **Bot Configuration** - Set up tennis court booking bots
2. **Court Monitoring** - Monitor available court slots
3. **Automated Booking** - Automatically book courts when available
4. **Manual Booking Flow** - Direct bot to specific page to select date, select court, fill form and complete booking

## API Endpoints

- `POST /bots` - Create bot configuration
- `GET /bots` - List all bots
- `POST /monitor` - Start court monitoring
- `POST /book` - Attempt to book court
- `GET /bookings/{id}` - Check booking status

## Development Guidelines

1. **Keep it simple** - No over-engineering
2. **Minimal changes** - Only implement what's requested
3. **No complex abstractions** - Direct, straightforward code