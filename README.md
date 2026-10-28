# Wolf’s Wisdom privacy policy

A static Russian privacy policy website for **Мудрость волка (Wolf’s Wisdom)**. Policy wording is copied from the app’s `app/src/main/assets/legal/privacy.txt` without rewriting it.

## Publish on GitHub Pages

1. Commit and push these files to the `main` branch of `missclick3/wolfwisdom-privacy-policy`.
2. In the GitHub repository, open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select **main** and **/ (root)**, then click **Save**.

Once GitHub finishes deployment, the policy will be available at:

https://missclick3.github.io/wolfwisdom-privacy-policy/

Use this address in the app store’s privacy policy field. The page is public, mobile-friendly, printable, and works without JavaScript, external fonts, or third-party assets.

## Preview

Open `index.html` directly in a browser, or run `python -m http.server 8000` in this directory and visit http://localhost:8000. Stop the server with Ctrl+C.

## Update the policy

1. Replace `privacy.txt` with the latest UTF-8 policy from the app. Preserve the existing `# Heading` and blank-line paragraph format.
2. Run `python scripts/build.py` to regenerate `index.html` (Python 3; no packages required).
3. Commit and push both files. GitHub Pages serves the prebuilt HTML; Python is only needed when updating the text.

`assets/app-icon.webp` is the existing app icon. All asset links are relative so the site works under the repository’s GitHub Pages path.
