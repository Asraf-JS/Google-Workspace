# Stage Capture Policy

User requirement: each screenshot shows only the current step and work already completed at that point.

Capture before advancing. Never build a finished workbook, deck or document and reuse that final state for earlier instructions. Later formulas, charts, tabs, review notes and outputs must be absent from earlier captures. Preserve an approved capture before changing the application state.

Distinguish supplied starter content/formatting from learner-created progress. Keep separate files for independent scenario copies. Place each image after the step it illustrates, with an exact stage caption.

Use real application captures. Crop or mask private account information without redrawing application content. Preserve menus with the native screenshot path; the browser clip capture path was observed to close a menu. Raw private captures and resource IDs stay outside the participant package.

User preference: retain the full application-window capture before making a crop, so framing can be adjusted later. Save an uncropped, original-dimension PNG with privacy masks in `_design/screenshots/full/`, and map it to the participant image in `_design/screenshots/manifest.json`. Keep the unredacted original locally. Do not overwrite either source when changing a crop.

For new captures, the entire visible window must match the current step, including outlines, tabs, slide thumbnails and neighbouring content. Reframe or recapture if later work appears outside the proposed crop. Do not rely on cropping to hide later learner-created objects. The retained historical source library explicitly flags exceptions and missing originals; it is an editing library, not blanket approval to use every entire frame in the lesson.

Record tool/feature fallbacks and untested routes accurately. A screenshot of a proposed access matrix is not a successful viewer-access test. Source uploads via the connector are not evidence that the browser upload interaction succeeded.
