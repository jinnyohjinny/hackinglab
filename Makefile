.PHONY: help start-level stop status list-levels stop-all

# Default target
help:
	@echo "DetectLab - Makefile Commands"
	@echo "=============================="
	@echo ""
	@echo "Usage:"
	@echo "  make start-level LEVEL=<number>  - Start a specific level (stops other running levels)"
	@echo "  make stop                        - Stop the currently running level"
	@echo "  make status                      - Check status of all levels"
	@echo "  make list-levels                 - List all available levels"
	@echo ""
	@echo "Examples:"
	@echo "  make start-level LEVEL=1"
	@echo "  make stop"
	@echo "  make status"

# List all available levels
list-levels:
	@echo "Available levels:"
	@for level in level-*; do \
		if [ -d "$$level" ] && [ -f "$$level/docker-compose.yml" ]; then \
			echo "  - $$level"; \
		fi \
	done

# Stop all running levels
stop-all:
	@echo "Stopping all running levels..."
	@for level in level-*; do \
		if [ -d "$$level" ] && [ -f "$$level/docker-compose.yml" ]; then \
			echo "Checking $$level..."; \
			cd "$$level" && docker-compose down 2>/dev/null || true; \
			cd ..; \
		fi \
	done
	@echo "All levels stopped."

# Start a specific level (stops others first)
start-level:
	@if [ -z "$(LEVEL)" ]; then \
		echo "Error: LEVEL parameter is required."; \
		echo "Usage: make start-level LEVEL=<number>"; \
		exit 1; \
	fi
	@if [ ! -d "level-$(LEVEL)" ]; then \
		echo "Error: level-$(LEVEL) does not exist."; \
		echo "Run 'make list-levels' to see available levels."; \
		exit 1; \
	fi
	@if [ ! -f "level-$(LEVEL)/docker-compose.yml" ]; then \
		echo "Error: level-$(LEVEL)/docker-compose.yml not found."; \
		exit 1; \
	fi
	@echo "Stopping all other running levels..."
	@for level in level-*; do \
		if [ -d "$$level" ] && [ -f "$$level/docker-compose.yml" ]; then \
			cd "$$level" && docker-compose down 2>/dev/null || true; \
			cd ..; \
		fi \
	done
	@echo ""
	@echo "Starting level-$(LEVEL)..."
	@cd level-$(LEVEL) && docker-compose up -d
	@echo ""
	@echo "✓ Level $(LEVEL) is now running!"
	@echo ""
	@echo "Container status:"
	@cd level-$(LEVEL) && docker-compose ps

# Stop the currently running level
stop:
	@echo "Checking for running levels..."
	@found=0; \
	for level in level-*; do \
		if [ -d "$$level" ] && [ -f "$$level/docker-compose.yml" ]; then \
			running_containers=$$(cd "$$level" && docker-compose ps --filter "status=running" -q 2>/dev/null | wc -l); \
			if [ "$$running_containers" -gt 0 ]; then \
				level_num=$${level#level-}; \
				echo "Stopping level $$level_num..."; \
				cd "$$level" && docker-compose down; \
				echo "✓ Level $$level_num stopped."; \
				found=1; \
				break; \
			fi; \
		fi; \
	done; \
	if [ $$found -eq 0 ]; then \
		echo "No running levels found."; \
	fi

# Check status of all levels
status:
	@echo "DetectLab - Level Status"
	@echo "========================"
	@echo ""
	@running=0; \
	for level in level-*; do \
		if [ -d "$$level" ] && [ -f "$$level/docker-compose.yml" ]; then \
			level_num=$${level#level-}; \
			running_containers=$$(cd "$$level" && docker-compose ps --filter "status=running" -q 2>/dev/null | wc -l); \
			if [ "$$running_containers" -gt 0 ]; then \
				echo "✓ Level $$level_num: RUNNING"; \
				(cd "$$level" && docker-compose ps 2>/dev/null | tail -n +2); \
				echo ""; \
				running=1; \
			fi; \
		fi; \
	done; \
	if [ $$running -eq 0 ]; then \
		echo "All levels are stopped."; \
	fi
