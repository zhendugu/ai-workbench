# Path Safety Guide for Vite Project

## Overview

Vite development server may have issues with paths containing certain special characters, particularly the `#` character, which is used in URL fragments.

## Current Status

✅ **Current project path is safe** - No illegal characters detected.

Path: `/Volumes/WD_BLACK_SN850X_2T/UsersData/chrislaw/Projects/ai-workbench/company_viewer`

## Checking Your Path

Run the path check script:
```bash
./check-path.sh
```

This will:
- Display the current project path
- Check for `#` and other problematic characters
- Report if the path is safe for Vite

## Common Issues

### Issue: Path contains `#` character

**Error message:**
```
The project root contains the "#" character (...) which may not work when running Vite.
```

**Solution:**
1. Identify which directory contains `#`
2. Rename the directory (remove or replace `#`)
3. Update project path references
4. Restart Vite dev server

### Issue: Other URL-unsafe characters

Characters that may cause issues:
- `#` (hash/fragment)
- `%` (URL encoding)
- `&` (URL parameter separator)
- Spaces (should use `-` or `_` instead)

## Best Practices

1. **Use simple directory names:**
   - ✅ `company_viewer`
   - ✅ `my-project`
   - ❌ `my#project`
   - ❌ `project with spaces`

2. **Check path before cloning/creating projects:**
   - Run `check-path.sh` in target directory
   - Avoid paths with special characters

3. **If you must use special characters:**
   - Replace with safe alternatives (`-`, `_`)
   - Or move project to a safe path location

## Troubleshooting

### Server starts but browser shows 404

1. Check the actual port number (may be different from 5173)
2. Check browser console for errors
3. Verify `index.html` exists in project root
4. Check Vite console output for warnings

### Path-related errors during build

1. Ensure no `#` in any parent directories
2. Check for symbolic links that may contain `#`
3. Verify absolute path doesn't contain problematic characters

## Verification

After any path changes, verify:
```bash
# 1. Check path is safe
./check-path.sh

# 2. Start dev server
npm run dev

# 3. Open browser to shown URL (usually http://localhost:5173)
# Should see application load successfully
```

## Additional Resources

- [Vite Documentation - Configuring Vite](https://vitejs.dev/config/)
- [URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.asp)

