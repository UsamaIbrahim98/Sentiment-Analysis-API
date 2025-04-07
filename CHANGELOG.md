## [1.1.0] - 7-4-2025
### Added
- Version endpoint (`/version`) to check API status
- Changelog endpoint (`/changelog`) to view updates
- Version number included in analysis responses
- Proper service name constant (`SERVICE_NAME`)

### Changed
- Renamed `/analyze-sentiment` endpoint to `/analyze` (simpler)
- Improved error response format
- Added documentation strings for all endpoints

### Fixed
- Better error handling for missing text input
- Consistent JSON response structure

## [1.0.0] - 7-4-2025  -->
### Added
- Initial sentiment analysis API
- Basic `/analyze-sentiment` endpoint