# Research Notes

## OWASP File Upload Security
File upload features may create security risks if uploaded files are not validated properly.

## Magic Byte Validation
Magic bytes are the first bytes of a file that help identify its real file type.

## Path Traversal
Path traversal is an attack where a user tries to access files outside the intended upload directory using values such as ../.

## Research Outcome
The reviewed security concepts were used as the foundation for designing and implementing the Lunarch Secure Uploader project.