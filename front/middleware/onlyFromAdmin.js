export default function ({$auth, redirect }) {
  if (!$auth.user) {
    return redirect('/login')
  }

  if (!$auth.user.is_admin) {
    return redirect('/')
  }
}
