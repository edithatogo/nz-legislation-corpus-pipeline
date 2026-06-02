# ChatGPT GitHub connector note

During this build session, the available GitHub connector actions exposed repository/search/read operations but not direct repository creation or bulk file push operations. The local setup script is therefore the safest setup path: it uses the official GitHub CLI from your authenticated machine to create the new repository, push this starter project, and configure Actions secrets/variables.
