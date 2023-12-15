# Specify the path to the parent directory
$parentDirectory = "C:\Users\shash\OneDrive\Desktop\Homework\4100FinalProject\Formatted Data"

# Specify the names of the subdirectories
$subdirectories = Get-ChildItem -Path $parentDirectory -Directory

foreach ($subdirectory in $subdirectories) {
    # Get the full path of the current subdirectory
    $subdirectoryPath = $subdirectory.FullName
    $dataQuery = Get-ChildItem -Path $subdirectoryPath
    foreach ($dq in $dataQuery) {
        $dq = Join-Path $dq.FullName 'images'
        Get-ChildItem -Path $dq | Move-Item -Destination $subdirectoryPath -Force
    }
    
    # Get all items from the current subdirectory and move them to the parent directory
    # Get-ChildItem -Path $subdirectoryPath | Move-Item -Destination $parentDirectory -Force
}

Write-Host "Files and folders moved successfully."
