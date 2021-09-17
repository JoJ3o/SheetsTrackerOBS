# SheetsTrackerOBS

Send data in Google Sheets over to OBS depending on what cell is active. Originally designed for KANNO's SM64 120Star SheetUnlimited steams.

## Todo

- Detect active cell
- Detect if active cell is in E column
- Detect if active cell in E column has a value on the same row of B
- If true, get value of A without the [x] part
- Round valueB to the nearest 0, 3 or 6 in the 2nd decimal after calculation

- Show nothing when active cell requirements aren't met
- Host format on website

- Detect active cell by specific user

## Format

{Title}:
Target={ValueB:0.95},PB={ValueE("??"if empty)}

**Example**
Chip off Whomp's Block (JP):
Target=31.43, PB=30.2
