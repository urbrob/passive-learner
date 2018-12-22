package passive_learner.urbrob.github.com.app

import android.content.Context

class FileManager(context: MainActivity) {
    private val ctx: MainActivity = context

    fun saveToLocalFile(fileName: String, content: String) {
        ctx.openFileOutput(fileName, Context.MODE_PRIVATE).use {
            it.write(content.toByteArray())
        }
    }
    fun deleteLocalFile(fileName: String) {
        ctx.deleteFile(fileName)
    }

}