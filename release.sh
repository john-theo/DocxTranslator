#!/bin/bash
set -e

if [ $# -ne 1 ]; then
  echo "Usage: $0 <version>"
  echo "Example: $0 0.1.1"
  exit 1
fi

VERSION=$1

# Update version in pyproject.toml
sed -i.bak "s/version = \"[0-9]*\.[0-9]*\.[0-9]*\"/version = \"$VERSION\"/" pyproject.toml
rm pyproject.toml.bak

# Update version in __init__.py
sed -i.bak "s/__version__ = \"[0-9]*\.[0-9]*\.[0-9]*\"/__version__ = \"$VERSION\"/" docx_translator/__init__.py
rm docx_translator/__init__.py.bak

# Commit changes
git add pyproject.toml docx_translator/__init__.py
git commit -m "🔖 Bump version to $VERSION"

# Create and push tag
git tag v$VERSION
git push origin main
git push origin v$VERSION

echo "Released version $VERSION"
echo "GitHub Actions will now build and publish packages" 