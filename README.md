# SkellyScan

SkellyScan is a powerful OSINT penetration testing tool designed for security researchers. It allows you to create and execute custom scanning workflows (skeletons) that can chain multiple security tools together in a sequential manner.

## Features

- **Customizable Workflows**: Create your own scanning skeletons using the Builder interface
- **Tool Chaining**: Automatically use results from one tool as input for the next
- **Project Management**: Organize scan results in dedicated project folders
- **Extensible**: Add your own tools to the engine folder
- **VPN Integration**: Optional Windscribe VPN support for anonymous scanning
- **feixdy Integration**: Iterate tools over multiple results using the feixdy.py utility

## Directory Structure

```
SkellyScan/
├── Builder/           # Interface for creating scanning presets
├── core/             # Core functionality and classes
├── engine/           # Default location for security tools
├── presets/          # Predefined scanning skeletons
├── projects/         # Output directory for scan results
└── wordlists/        # Wordlists for various tools
```

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python skelly.py -d target.com -p preset_name
```

### Command Line Options

- `-d, --domain`: Target domain to scan
- `-p, --preset`: Preset scan .ini file to run
- `-vpn, --vpn`: Cycle through Windscribe VPN servers (set >= 15 to enable)
- `-v, --verbose`: Enable verbose output

### Creating Custom Presets

Presets are defined in .ini files in the `presets/` directory. Each preset contains:
- A list of tools to run
- Parameters for each tool
- Dependencies between tools (using results from previous scans)

Example preset structure:
```ini
[DEFAULT]
Info: Quick lib of all keys
1: _NOHTTPDOMAINNAME_
2: _DOMAINNAME_
3: _PROJECTLIB_
4: _TIMESTAMP_

[1]
tool=sublister
task=-d _NOHTTPDOMAINNAME_ -o projects\_PROJECTLIB_\Subdomains.txt
[2]
tool=ffuf
task=-u _DOMAINNAME_/FUZZ -o projects\_PROJECTLIB_\FFUF_Fuzzed.csv -of csv -w wordlists\fuzzdirectories\others.txt
```

### Using feixdy.py

feixdy.py allows you to iterate a tool over multiple results from a previous scan:

```bash
python feixdy.py -i input_file -t tool_name -ta tool_arguments [-f field_name]
```

## Adding New Tools

1. Add your tool to the `engine/` directory
2. Create a new preset in the `presets/` directory
3. Define the tool's parameters and dependencies in the preset

## Security Note

This tool is intended for authorized security testing only. Always ensure you have permission to scan the target systems.

## License

[Add your license information here]