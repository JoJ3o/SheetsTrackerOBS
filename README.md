# SheetsTrackerOBS

Send data in Google Sheets over to OBS depending on what cell is active. Originally designed for KANNO's SM64 120Star SheetUnlimited steams.

## Todo

- ✓Detect active cell
- ✓Detect if active cell is in E column
- ✓Detect if active cell in E column has a value on the same row of B
- If true, get value of A without the [x] part
- Round valueB to the nearest 0, 3 or 6 in the 2nd decimal after calculation

- Show nothing when active cell requirements aren't met
- Host format on website

- Detect active cell by specific user

- Access flask app from phone
- Access flask from different network (portforwarding)
- Remove "[1]" from name
- Automatically update data from change in google sheet or every few seconds (help from gilde)

## Format

{Title}:
Target={ValueB:0.95},PB={ValueE("??"if empty)}

**Example**
Chip off Whomp's Block (JP):
Target=31.43, PB=30.2

## Test

Correct info at:

- Single X in correct column (data)
- Single X in wrong column (nothing/empty)
- Single X at empty pb ("??" at pb)
- Multiple X's
- Friend's computer entering website
-
